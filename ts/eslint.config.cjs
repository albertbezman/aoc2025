// eslint.config.cjs – flat config for TypeScript + Prettier (Node environment)

const tseslint = require("typescript-eslint");
const prettier = require("eslint-config-prettier");

/** @type {import("eslint").Linter.FlatConfig[]} */
module.exports = tseslint.config(
  // 1) Global settings / ignores
  {
    ignores: ["dist/", "node_modules/", "eslint.config.cjs"],
  },

  // 2) Recommended TS rules
  ...tseslint.configs.recommended,

  // 3) Disable stylistic rules that conflict with Prettier
  prettier,

  // 4) Project-specific overrides
  {
    languageOptions: {
      globals: {
        require: "readonly",
        module: "readonly",
        __dirname: "readonly",
        process: "readonly",
      },
    },
    rules: {
      // Allow Node-style require() in your TS files
      "@typescript-eslint/no-require-imports": "off",
    },
  }
);

