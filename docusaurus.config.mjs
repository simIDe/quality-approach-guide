// Docusaurus configuration for the Quality Approach guide site.
// English is the default language; French lives in i18n/fr/.
// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

const repo = 'https://github.com/simIDe/quality-approach-guide';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Quality Approach: mini-project guide',
  tagline: 'Deliver a simple data product, with method',
  url: 'https://simide.github.io',
  baseUrl: '/quality-approach-guide/',
  organizationName: 'simIDe',
  projectName: 'quality-approach-guide',
  trailingSlash: false,

  // Strict build: a broken link or anchor fails the build.
  onBrokenLinks: 'throw',
  onBrokenAnchors: 'throw',
  onDuplicateRoutes: 'throw',
  markdown: {
    // .md files are read as plain Markdown, .mdx files as MDX.
    format: 'detect',
    hooks: {onBrokenMarkdownLinks: 'throw'},
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'fr'],
    localeConfigs: {
      en: {label: 'English', htmlLang: 'en'},
      fr: {label: 'Français', htmlLang: 'fr'},
    },
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.mjs',
          editUrl: `${repo}/edit/main/`,
          showLastUpdateTime: true,
        },
        blog: false,
        theme: {customCss: './src/css/custom.css'},
      }),
    ],
  ],

  themes: [
    [
      // Local search: the index is built with the site, no third-party service.
      '@easyops-cn/docusaurus-search-local',
      {hashed: true, language: ['en', 'fr'], docsRouteBasePath: '/', indexBlog: false},
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Quality Approach',
        items: [
          {type: 'localeDropdown', position: 'right'},
          {href: repo, label: 'GitHub', position: 'right'},
        ],
      },
      footer: {
        style: 'light',
        copyright:
          'Master 2 STAPS, UFR STAPS Montpellier. Texts under CC BY 4.0, code under the MIT licence.',
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['bash', 'powershell', 'sql', 'yaml', 'toml'],
      },
    }),
};

export default config;
