import time  # Importation du module time pour mesurer le temps d'exécution

def measure_time(func, *args, **kwargs):
    """
    Fonction pour mesurer le temps d'exécution d'une fonction donnée.
    
    Paramètres :
    func : fonction à exécuter
    *args : arguments positionnels de la fonction
    **kwargs : arguments nommés de la fonction
    
    Retourne :
    - Le résultat de la fonction
    - Le temps d'exécution en secondes
    """
    start = time.perf_counter()  # Démarre le chronomètre haute précision
    result = func(*args, **kwargs)  # Exécute la fonction avec les arguments fournis
    end = time.perf_counter()  # Arrête le chronomètre
    return result, end - start  # Retourne le résultat et le temps écoulé

def print_comparison_table(bt_result, bt_time, bf_result, bf_time):
    """
    Fonction pour afficher un tableau comparatif des performances entre deux méthodes.
    
    Paramètres :
    bt_result : Résultat de la méthode Backtracking
    bt_time : Temps d'exécution de la méthode Backtracking
    bf_result : Résultat de la méthode Force Brute
    bf_time : Temps d'exécution de la méthode Force Brute
    """
    print("\n📊 Comparaison des performances :\n")  # Affiche un titre avec un emoji
    
    # Affichage de l'en-tête du tableau avec un formatage aligné
    print(f"{'Méthode':<20}{'Succès':<10}{'Temps (s)':<10}")  
    print("-" * 40)  # Séparateur visuel
    
    # Affichage des résultats des deux méthodes avec formatage
    print(f"{'Backtracking':<20}{str(bt_result):<10}{bt_time:.4f}")
    print(f"{'Force Brute':<20}{str(bf_result):<10}{bf_time:.4f}")
