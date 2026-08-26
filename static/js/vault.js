/**
 * AETHER JEWELS – Private Client Vault / Wishlist Manager
 */

const CelestialVault = (function () {
  let vaultItems = [];

  function init() {
    try {
      vaultItems = JSON.parse(localStorage.getItem('aether_vault')) || [];
    } catch (e) {
      vaultItems = [];
    }
    updateVaultUI();
    bindEvents();
  }

  function save() {
    localStorage.setItem('aether_vault', JSON.stringify(vaultItems));
    updateVaultUI();
  }

  function toggleItem(product) {
    const idx = vaultItems.findIndex(item => item.id === product.id);
    let added = false;

    if (idx > -1) {
      vaultItems.splice(idx, 1);
      if (window.showToast) window.showToast(`Removed "${product.title}" from your Private Vault.`, 'info');
    } else {
      vaultItems.push(product);
      added = true;
      if (window.showToast) window.showToast(`Archived "${product.title}" to your Private Vault.`, 'success');
    }

    save();
    return added;
  }

  function removeItem(id) {
    vaultItems = vaultItems.filter(item => item.id !== id);
    save();
    renderVaultPage();
  }

  function isSaved(id) {
    return vaultItems.some(item => item.id === id);
  }

  function updateVaultUI() {
    // Update badge counter in nav
    const badges = document.querySelectorAll('.vault-count-badge');
    badges.forEach(b => {
      b.textContent = vaultItems.length;
      b.style.display = vaultItems.length > 0 ? 'flex' : 'none';
    });

    // Update buttons state
    document.querySelectorAll('.card-vault-btn').forEach(btn => {
      const id = parseInt(btn.dataset.productId);
      if (isSaved(id)) {
        btn.classList.add('saved');
        btn.innerHTML = '<i class="ri-heart-3-fill"></i>';
      } else {
        btn.classList.remove('saved');
        btn.innerHTML = '<i class="ri-heart-3-line"></i>';
      }
    });
  }

  function bindEvents() {
    document.addEventListener('click', (e) => {
      const btn = e.target.closest('.card-vault-btn');
      if (btn) {
        e.preventDefault();
        e.stopPropagation();

        const product = {
          id: parseInt(btn.dataset.productId),
          title: btn.dataset.productTitle,
          price_inr: parseFloat(btn.dataset.productPrice),
          image: btn.dataset.productImage,
          url: btn.dataset.productUrl,
          specs: btn.dataset.productSpecs || '',
        };

        toggleItem(product);
      }
    });
  }

  function renderVaultPage() {
    const container = document.getElementById('vault-items-container');
    const emptyState = document.getElementById('vault-empty-state');
    if (!container) return;

    if (vaultItems.length === 0) {
      container.innerHTML = '';
      if (emptyState) emptyState.style.display = 'block';
      return;
    }

    if (emptyState) emptyState.style.display = 'none';

    container.innerHTML = vaultItems.map(item => `
      <div class="product-card glass-card">
        <div class="product-img-wrapper">
          <img src="${item.image}" alt="${item.title}" class="product-img-primary">
          <button class="card-vault-btn saved" onclick="CelestialVault.remove(${item.id})">
            <i class="ri-delete-bin-line"></i>
          </button>
        </div>
        <div class="product-card-body">
          <div>
            <h3 class="product-card-title">${item.title}</h3>
            <p class="product-card-specs">${item.specs}</p>
          </div>
          <div class="product-card-footer">
            <span class="product-price-val" data-price-inr="${item.price_inr}">${CurrencyConverter.convert(item.price_inr)}</span>
            <a href="${item.url}" class="btn btn-outline-gold btn-sm">Inspect Jewel</a>
          </div>
        </div>
      </div>
    `).join('');

    if (window.CurrencyConverter) {
      window.CurrencyConverter.refresh();
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    init();
    if (document.getElementById('vault-items-container')) {
      renderVaultPage();
    }
  });

  return {
    toggle: toggleItem,
    remove: removeItem,
    isSaved: isSaved,
    getAll: () => vaultItems,
  };
})();
