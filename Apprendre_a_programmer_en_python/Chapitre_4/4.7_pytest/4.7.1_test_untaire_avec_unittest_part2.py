
#   Les principales méthode d'assertion


methode = [
    "assertEqual(a, b)",
    "assertNotEqual(a, b)",
    "assertTrue(x)",
    "assertFalse(x)",
    "assertIs(a, b)",
    "assertIsNot(a, b)",
    "assertIsNone(x)",
    "assertIsNotNone(x)",
    "assertIn(a, b)",
    "assertNotIn(a, b)",
    "assertIsInstance(a, b)",
    "assertNotIsInstance(a, b)",
    "assertRaises(exception, fonction, *args, **kwargs) ",  
    ]

explications = [
    "a == b",
    "a != b",
    "x is True",
    "x is False",
    "a is b",
    "a is not b",
    "x is None",
    "x is not None",
    "a in b",
    "a not in b",
    "isinstance(a, b)",
    "not isinstance(a, b)",
    "Vérifie que la fonction lève l'exception attendue.",
    ]

print("Liste de Methode : {} \n \
        Explications correspondante: {}\n".format(methode, explications))
