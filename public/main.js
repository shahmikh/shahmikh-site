(function () {
  "use strict";

  // ---- Sticky header background on scroll ----
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      if (window.scrollY > 12) {
        header.classList.add("is-scrolled");
      } else {
        header.classList.remove("is-scrolled");
      }
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // ---- Mobile nav toggle ----
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var expanded = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!expanded));
      links.classList.toggle("is-open");
    });
    links.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        toggle.setAttribute("aria-expanded", "false");
        links.classList.remove("is-open");
      });
    });
  }

  // ---- Scroll reveal ----
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: "0px 0px -60px 0px" }
    );
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }

  // ---- Social links: hidden until a real URL is set -----------------------
  // To switch them on, replace href="#" on the YouTube / Instagram links
  // (class "social-link") in the HTML files with your real channel / profile URLs.
  document.querySelectorAll(".social-link").forEach(function (a) {
    var href = a.getAttribute("href");
    if (!href || href === "#") {
      var li = a.closest("li");
      (li || a).style.display = "none";
    }
  });
  document.querySelectorAll(".social-section").forEach(function (sec) {
    var live = sec.querySelectorAll('.social-link:not([href="#"])');
    if (!live.length) sec.style.display = "none";
  });
})();
