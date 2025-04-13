from dataclasses import dataclass


@dataclass
class MapNames:
    romanian: str
    english: str
    japanese: str


class Maps:
    hedate = MapNames(
        romanian="hedate", english="Windward Plains", japanese="隔ての砂原"
    )
    hinomori = MapNames(
        romanian="hinomori", english="Scarlet Forest", japanese="緋の森"
    )
    yuwaki = MapNames(romanian="yuwaki", english="Oilwell Basin", japanese="油涌き谷")
    hyoumu = MapNames(
        romanian="hyoumu", english="Iceshard Cliffs", japanese="氷霧の断崖"
    )
    ryuto = MapNames(
        romanian="ryuto", english="Ruins of Wyveria", japanese="竜都の跡形"
    )


if __name__ == "__main__":
    # print('activated main part of "mytypes.py"')
    maps = Maps()
    print(maps.hedate)
    print(maps.hedate.romanian)
    print(maps.hedate.english)
    print(maps.hedate.japanese)
