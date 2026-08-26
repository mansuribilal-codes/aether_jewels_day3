/**
 * AETHER JEWELS – Global Luxury Currency Switcher
 * Supports INR (₹ default with Lakhs/Crores), USD ($), EUR (€), AED (د.إ), GBP (£)
 */

const CurrencyConverter = (function () {
  const RATES = {
    INR: { symbol: '₹', rate: 1.0, formatIndian: true },
    USD: { symbol: '$', rate: 0.012, formatIndian: false },
    AED: { symbol: 'AED ', rate: 0.044, formatIndian: false },
    GBP: { symbol: '£', rate: 0.0094, formatIndian: false },
    EUR: { symbol: '€', rate: 0.011, formatIndian: false },
  };

  let currentCurrency = localStorage.getItem('aether_currency') || 'INR';

  function init() {
    updateCurrencyUI();
    bindCurrencyModal();
  }

  function setCurrency(code) {
    if (!RATES[code]) return;
    currentCurrency = code;
    localStorage.setItem('aether_currency', code);
    updateCurrencyUI();
    convertAllPricesOnPage();

    if (window.showToast) {
      window.showToast(`Display currency adjusted to ${code} (${RATES[code].symbol})`, 'info');
    }
  }

  function formatIndianCurrency(amountInInr) {
    const amt = Math.round(amountInInr);
    if (amt >= 10000000) {
      return `₹ ${(amt / 10000000).toFixed(2)} Cr`;
    } else if (amt >= 100000) {
      return `₹ ${(amt / 100000).toFixed(2)} Lakhs`;
    } else {
      return `₹ ${amt.toLocaleString('en-IN')}`;
    }
  }

  function convertPrice(inrAmount) {
    if (!inrAmount || isNaN(inrAmount)) return '';
    const config = RATES[currentCurrency] || RATES.INR;

    if (currentCurrency === 'INR') {
      return formatIndianCurrency(inrAmount);
    }

    const converted = Math.round(inrAmount * config.rate);
    return `${config.symbol}${converted.toLocaleString('en-US')}`;
  }

  function convertAllPricesOnPage() {
    document.querySelectorAll('[data-price-inr]').forEach((el) => {
      const inr = parseFloat(el.getAttribute('data-price-inr'));
      if (!isNaN(inr)) {
        el.textContent = convertPrice(inr);
      }
    });
  }

  function updateCurrencyUI() {
    document.querySelectorAll('.current-currency-symbol').forEach(el => {
      el.textContent = currentCurrency;
    });

    document.querySelectorAll('.currency-option-btn').forEach(btn => {
      if (btn.dataset.currency === currentCurrency) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }

  function bindCurrencyModal() {
    document.querySelectorAll('.currency-option-btn').forEach(btn => {
      btn.addEventListener('click', function () {
        const code = this.dataset.currency;
        setCurrency(code);
        const modal = document.getElementById('currency-modal');
        if (modal) modal.classList.remove('open');
      });
    });
  }

  document.addEventListener('DOMContentLoaded', init);

  return {
    get: () => currentCurrency,
    set: setCurrency,
    convert: convertPrice,
    refresh: convertAllPricesOnPage,
  };
})();
