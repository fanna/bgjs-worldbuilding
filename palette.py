import tcod as libtcod

tree = {'bg': libtcod.Color(156, 219, 67), 'fg': libtcod.Color(89, 193, 53)}
sea = {'bg': libtcod.Color(36, 159, 222), 'fg': libtcod.Color(40, 92, 196)}
dirt  = {'bg': libtcod.Color(244, 210, 156), 'fg': libtcod.Color(187, 117, 71)}
mountain  = {'fg': libtcod.Color(139, 147, 175), 'bg': libtcod.Color(90, 78, 68)}
high_mountain  = {'fg': libtcod.Color(255, 255, 255), 'bg': libtcod.Color(139, 147, 175)}
grass = {'fg': libtcod.Color(26, 122, 62), 'bg': libtcod.Color(89, 193, 53)}
sand = {'fg': libtcod.Color(244, 210, 156), 'bg': libtcod.Color(254, 243, 192)}
deep_sea = {'fg': libtcod.Color(20, 52, 100), 'bg': libtcod.Color(40, 92, 196)}

palette = [tree, sea, dirt, mountain, high_mountain, grass, sand, deep_sea]

book = """      ,   ,

     /////|

    ///// |

   |~~~|  |

   |===|  |

   |M  |  |

   | A |  |

   |  G| /

   |===|/

   '---'"""

compass = """
      N

      |

      |

     =|=
 W----o----E
     =|=

      |

      |

      S"""
