class Project:
    def __init__(self, cost_of_hours):
        self.__project_cost = 0
        self.__cost_of_hours = cost_of_hours

    def get_cost(self, project_times):
        # ["1 year", "12 weeks", "20 days", "3 hours"]
        # 1 hour = 50euros
        #calculate project cost

        hours = 0

        for text in project_times:
            # ["1", "year"]
            list = text.split(" ")
            time = list[1]
            amount = int(list[0])
            if time == "year" or time == "years":
                hours = hours + (24 * 30 * 12) * amount
            elif time == "months" or time == "month":
                hours = hours + (30 * 24) * amount
            elif time == "week" or time == "weeks":
                hours = hours + (7 * 24) * amount
            elif time == "days" or time == "day":
                hours = hours + 24 * amount
            elif time == "hours" or time == "hour":
                hours = hours + amount
            else:
                raise Exception("Invalid time format")

        self.__project_cost = hours * self.__cost_of_hours
        return self.__project_cost