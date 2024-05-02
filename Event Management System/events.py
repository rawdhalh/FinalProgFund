class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company=None, cleaning_company=None, decorations_company=None, entertainment_company=None, furniture_company=None, invoice=None):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decorations_company = decorations_company
        self.entertainment_company = entertainment_company
        self.furniture_company = furniture_company
        self.invoice = invoice
        self.caterer = caterer
        self.venue = venue
        self.suppliers = suppliers

    def __str__(self):
        return f"Event ID: {self.event_id}\nEvent Type: {self.event_type}\nTheme: {self.theme}\nDate: {self.date}\nTime: {self.time}\nDuration: {self.duration}\nVenue Address: {self.venue_address}\nClient ID: {self.client_id}\nGuest List: {', '.join(self.guest_list)}\nCatering Company: {self.catering_company}\nCleaning Company: {self.cleaning_company}\nDecorations Company: {self.decorations_company}\nEntertainment Company: {self.entertainment_company}\nFurniture Company: {self.furniture_company}\nInvoice: {self.invoice}"