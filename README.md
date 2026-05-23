# Test Titans — Hybrid Test Automation Framework

A streamlined **Hybrid Test Automation Framework** engineered for End-to-End (E2E) UI and API testing on the [AutomationExercise](https://automationexercise.com) platform. It utilizes the Page Object Model (POM) design pattern alongside behavior-driven development principles to deliver clean, scalable, and modular test coverage.

---

## 🚀 Key Framework Features

* **Hybrid Verification:** Seamlessly executes browser-based UI automation scenarios concurrently with backend REST API request validations.
* **Page Object Model (POM):** Decouples page interaction mechanisms and web element definitions from behavioral verification steps.
* **Ad-Blocking Interception:** Features an embedded script injection layer designed to remove disruptive third-party iframes and overlay elements, eliminating test flakiness during browser navigation.
* **Dynamic Registrations:** Avoids database constraint limitations by dynamically tracking user data values via runtime generation tools during account setup loops.
* **Centralized Configuration:** Isolates environmental variables, test endpoints, wait thresholds, and browser choices from the functional code footprint.

---

## 📂 Core Project Hierarchy

* **`data/`**: Configuration manifests defining browser execution options and primary target applications.
* **`features/`**: Human-readable Gherkin DSL test scenarios mapping operational lifecycle actions and behaviors.
* **`features/steps/`**: Modular behavioral step verification scripts mapping test instructions to page behaviors.
* **`pages/`**: Structured page view components defining element identifiers and target business logic workflows.
* **`utils/`**: Driver setup classes and property files handling browser binary setups and config handling.

---

## ⚙️ Prerequisites & Setup

1. **Environment Setup:** Ensure Python 3.11+ is configured inside a virtual environment.
2. **Dependency Configuration:** Install required alignment boundaries using the pinned project library manifest.
3. **Automated Drivers:** Browser instances deploy automatically via contextual managers matching your active system environment.

---

## 🏃 Execution Profiles

* **Execute All BDD Specifications:** Parse feature sets and track user actions across all standard feature layers.
* **Target Specific Subsets:** Group functional execution using custom label tags (e.g., isolating smoke verification checkpoints).
* **Execute API Directives:** Verify isolated backend API services independently.
* **Test Reporting:** Review HTML output metrics generated inside the project dashboard folders following execution completion.
