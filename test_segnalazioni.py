"""Test dei difetti segnalati dalla segreteria."""

import unittest
from datetime import date

from prenotazioni import Agenda, Prenotazione, Sala
class TestSegnalazioni(unittest.TestCase):
    def test_prenotazioni_contigue(self):
        # Preparazione
        agenda = Agenda()
        agenda.aggiungi_sala(Sala("A2", "Aula 2", 25))

        oggi = date(2026, 11, 2)
        giorno = date(2026, 11, 3)

        prima = Prenotazione("A2", giorno, "09:00", "10:00", "Rossi", 5)
        seconda = Prenotazione("A2", giorno, "10:00", "11:00", "Bianchi", 5)

        agenda.prenota(prima, oggi=oggi)

        # Azione
        risultato = agenda.prenota(seconda, oggi=oggi)

        # Verifica
        self.assertEqual(risultato, 2)
if __name__ == "__main__":
    unittest.main()