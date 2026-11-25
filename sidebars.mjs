// Navigation du site. Les dossiers fiches/ et modeles/ sont listés automatiquement.
// scripts/verifier-navigation.mjs vérifie qu'aucune page de docs/ n'est oubliée ici.
// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  guide: [
    'index',
    {
      type: 'category',
      label: 'Le mini-projet',
      collapsed: false,
      items: ['idees-de-projets'],
    },
  ],
};

export default sidebars;
