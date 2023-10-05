from battery import Battery

def SplinderBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.need_service_year=2

    def needs_service(self):
        service_due_date = self.last_service_date + self.need_service_year
        if(self.current_date > service_due_date):
            return True
        else:
            return False