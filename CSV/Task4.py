"""
Повторение - мать учения.
Достаньте имя из словаря
"""
super_dificult_dict = {
    1: {
        "pochti": {
            "Esche chutka": {
                ("Eto", "Chto?", "kortezh??"): {
                    "za chto???": [[1, 2, 3], ["1", 2, (13, "oleg")]]
                }
            }
        }
    }
}
first = super_dificult_dict.get(1)
second = first.get("pochti")
third = second.get("Esche chutka")
four = third.get(("Eto", "Chto?", "kortezh??"))
fifth = four.get("za chto???")
print(fifth[1][2][1])
