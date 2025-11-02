from data.config import HangmanVisualizerLevel

class HangmanVisualizer:
    def __init__(self, level: str):
        self._config = self._create_confing()
        self._level = level

    @classmethod
    def _create_confing(cls):
        return HangmanVisualizerLevel

    def get_visualization(self, attempts_used: int):
        _HANGMAN_STAGES = [
    """
------
|    |
|    O
|   /|\\
|   / \\
|    
----------
""",
    """
------
| 
|    
|    O
|   /|\\
|   / \\
----------
""",
    """
---
| 
|    
|    O
|   /|\\
|   / \\
----------
""",
    """
    
    
|    
|    O
|   /|\\
|   / \\
----------
""",
    """
    
    
           
|    O
|   /|\\
|   / \\
----------
""",
    """
    
              
               
     O
    /|\\
|   / \\
----------
""",
    """
                 
                
            
     O
    /|\\
    / \\
----------
"""
]
        config = self._config[self._level].value

        return _HANGMAN_STAGES[config[attempts_used]]


