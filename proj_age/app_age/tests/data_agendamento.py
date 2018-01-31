
reg1 = \
{
    "in":
    {
        "data": "2019-01-31",
        "hora_inicial": "8:00",
        "hora_final": "9:00",
        "paciente": "Felipe",
    },
    "out":
    {
        "data": "2019-01-31",
        "hora_inicial": "08:00:00",
        "hora_final": "09:00:00",
        "paciente": "Felipe",
        "procedimento": "consulta",
    },
}


reg2 = \
{
    "in":
    {
        "data": "2019-01-31",
        "hora_inicial": "9:15",
        "hora_final": "9:45",
        "paciente": "Fernando",
        "procedimento": "exame próstata",
    },
    "out":
    {
        "data": "2019-01-31",
        "hora_inicial": "09:15:00",
        "hora_final": "09:45:00",
        "paciente": "Fernando",
        "procedimento": "exame próstata",
    },
}


reg3 = \
{
    "in":
    {
        "data": "2019-02-01",
        "hora_inicial": "9:15",
        "hora_final": "9:45",
        "paciente": "Luis",
        "procedimento": "exame vista",
    },
    "out":
    {
        "data": "2019-02-01",
        "hora_inicial": "09:15:00",
        "hora_final": "09:45:00",
        "paciente": "Luis",
        "procedimento": "exame vista",
    },
}


reg_invalid_date = \
{
    "in":
    {
        "data": "2019-01-32",
        "hora_inicial": "10:15",
        "hora_final": "10:45",
        "paciente": "Fernando",
    },
    "out":
    {
        "data": [
            "Date has wrong format. Use one of these formats instead: YYYY[-MM[-DD]]."
        ]
    },
}


reg_not_unique = \
{
    "in":
    {
        "data": "2019-02-01",
        "hora_inicial": "10:15",
        "hora_final": "10:45",
        "paciente": "Paulo",
    },
    "out":
    {
        "non_field_errors": [
            "The fields data, hora_inicial must make a unique set."
        ]
    }
}


reg_blank = \
{
    "in":
    {
        "data": "",
        "hora_inicial": "",
        "hora_final": "",
        "paciente": "",
    },
    "out":
    {
        "data": [
            "Date has wrong format. Use one of these formats instead: YYYY[-MM[-DD]]."
        ],
        "hora_inicial": [
            "Time has wrong format. Use one of these formats instead: hh:mm[:ss[.uuuuuu]]."
        ],
        "hora_final": [
            "Time has wrong format. Use one of these formats instead: hh:mm[:ss[.uuuuuu]]."
        ],
        "paciente": [
            "This field may not be blank."
        ]
    }
}


reg_hora_inicial_maior_hora_final = \
{
    "in":
    {
        "data": "2019-03-30",
        "hora_inicial": "10:20",
        "hora_final": "10:00",
        "paciente": "Airton",
    },
    "out":
    {
        "non_field_errors": [
            "O horário final da consulta deve ser depois do inicial"
        ]
    },
}


reg_list = \
{
    "out":
    [
        reg1['out'],
        reg2['out'],
    ]
}

reg_list2 = \
{
    "out":
    [
        reg3['out'],
    ]
}
