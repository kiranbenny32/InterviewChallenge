import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import Manager, Coach, Player, Team, Fixture


def registration_form(request):
    return render(request, "registration_form.html")


def registration(request):
    if request.method == "POST":
        data = json.loads(request.body)["data"]

        team_obj = Team(name=data["team_name"])
        team_obj.save()

        manager_obj = Manager(name=data["manager_name"], team=team_obj)
        manager_obj.save()

        coach_obj = Coach(name=data["coach_name"], team=team_obj)
        coach_obj.save()

        for player_name in data["players_name"]:
            player_obj = Player(name=player_name, team=team_obj)
            player_obj.save()
        return HttpResponse("Team " + team_obj.name + " Created Successfully")

    elif request.method == "GET":
        if len(Team.objects.all()) < 10:
            return render(request, "registration_form.html")

        elif len(Team.objects.all()) == 10:

            def fixtures(teams):
                rotation = list(teams)

                fixtures = []
                for i in range(0, len(teams) - 1):
                    fixtures.append(rotation)
                    rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

                return fixtures

            # demo code
            teams = []
            for i in Team.objects.all():
                teams.append(i.name)

            # for one match each - use this block only
            matches = fixtures(teams)
            fixtures_list = []
            for f in matches:
                for a in zip(*[iter(f)] * 2):
                    fixtures_list.append(a)

            print(fixtures_list[0])

            from datetime import timedelta, date

            def daterange(start_date, end_date):
                for n in range(int((end_date - start_date).days)):
                    yield start_date + timedelta(n)

            start_date = date(2020, 11, 1)
            end_date = date(2020, 11, 20)
            for single_date in daterange(start_date, end_date):
                matches=1
                while len(fixtures_list) > 0:
                    if matches<2:
                        matches = matches + 1
                        team_count = 1
                        for f in fixtures_list:
                            if team_count <= 2:
                                print(f[0] + " " + f[1]+" "+str(single_date))
                                team_count = team_count + 1
                            else:
                                fixtures_list.remove(fixtures_list[0])
                                fixtures_list.remove(fixtures_list[1])

                                break
                    else:
                        break


            return HttpResponse("<h2>Registration finished</h2>")

        else:
            return HttpResponse("<h2>Registration finished</h2>")
