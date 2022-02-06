type_table = {
  #from https://i.imgur.com/6OXQ7i0.png

  'normal': {
    'weaknesses': ['fighting'],
    'resistances': [],
    'immunities': ['ghost']
  },

  'flying': {
    'weaknesses': ['electric','rock','ice'],
    'resistances': ['grass','fighting','bug'],
    'immunities': ['ground']
  },

  'ground': {
    'weaknesses': ['water','grass','ice'],
    'resistances': ['rock','poison'],
    'immunities': ['electric']
  },

  'bug': {
    'weaknesses':['fire','rock','flying'],
    'resistances': ['ground','grass','fighting'],
    'immunities': []
  },

  'steel': {
    'weaknesses':['fire','fighting','ground'],
    'resistances': ['normal','ice','grass','flying','fairy','dragon','bug','steel','rock','psychic'],
    'immunities': ['poison']
  },

  'water': {
    'weaknesses': ['grass','electric'],
    'resistances': ['water','steel','ice','fire'],
    'immunities': []
  },

  'electric': {
    'weaknesses': ['ground'],
    'resistances': ['steel','flying','electric'],
    'immunities': []
  },

  'ice': {
    'weaknesses': ['steel','rock','fire','fighting'],
    'resistances': ['ice'],
    'immunities': []
  },

  'fighting': {
    'weaknesses': ['psychic','flying','fairy'],
    'resistances': ['rock','bug','dark'],
    'immunities': []
  },

  'poison': {
    'weaknesses':['psychic','ground'],
    'resistances': ['poison','grass','fighting','fairy','bug'],
    'immunities': []
  },

  'rock': {
    'weaknesses': ['water','steel','ground','grass','fighting'],
    'resistances': ['poison','normal','flying','fire'],
    'immunities': []
  },

  'ghost': {
    'weaknesses': ['ghost','dark'],
    'resistances': ['poison','bug'],
    'immunities': ['normal','fighting']
  },

  'fire': {
    'weaknesses': ['water','ground','rock'],
    'resistances': ['steel','ice','grass','fire','fairy','bug'],
    'immunities': []
  },

  'grass': {
    'weaknesses': ['flying','bug','ice','fire','poison'],
    'resistances': ['water','ground','grass','electric'],
    'immunities': []
  },

  'psychic': {
    'weaknesses': ['ghost','dark','bug'],
    'resistances': ['psychic','fighting'],
    'immunities': []
  },

  'dragon': {
    'weaknesses':['ice','fairy','dragon'],
    'resistances': ['water','fire','grass','electric'],
    'immunities': []
  },

  'fairy': {
    'weaknesses': ['steel','poison'],
    'resistances': ['fighting','dark','bug'],
    'immunities': ['dragon']
  }
}


