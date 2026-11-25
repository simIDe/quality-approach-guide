// Configuration du site Docusaurus du guide « Quality Approach ».
// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

const repo = 'https://github.com/simIDe/quality-approach-guide';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Quality Approach : guide du mini-projet',
  tagline: 'Livrer un data product simple, avec méthode',
  url: 'https://simide.github.io',
  baseUrl: '/quality-approach-guide/',
  organizationName: 'simIDe',
  projectName: 'quality-approach-guide',
  trailingSlash: false,

  // Vérification stricte : un lien ou une ancre cassés font échouer la construction.
  onBrokenLinks: 'throw',
  onBrokenAnchors: 'throw',
  onDuplicateRoutes: 'throw',
  markdown: {
    // Les fichiers .md sont lus comme du Markdown standard, les .mdx comme du MDX.
    format: 'detect',
    hooks: {onBrokenMarkdownLinks: 'throw'},
  },

  i18n: {defaultLocale: 'fr', locales: ['fr']},

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.js',
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
      // Recherche locale : l'index est construit avec le site, sans service tiers.
      '@easyops-cn/docusaurus-search-local',
      {hashed: true, language: ['fr'], docsRouteBasePath: '/', indexBlog: false},
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Quality Approach',
        items: [{href: repo, label: 'GitHub', position: 'right'}],
      },
      footer: {
        style: 'light',
        copyright:
          'Master 2 STAPS, UFR STAPS Montpellier. Textes sous licence CC BY 4.0, code sous licence MIT.',
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['bash', 'powershell', 'sql', 'yaml', 'toml'],
      },
    }),
};

export default config;
