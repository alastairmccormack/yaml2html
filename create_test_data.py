import models

data = models.Directory(
    entries=[
        models.DirectoryEntry(
            name='Banana Man',
            phone=['+441234'],
            address=models.Address(
                lines=['29 Acacia Road', 'Nuttytown'],
                post_code='BA7 2AN'
            )
        ),
        models.DirectoryEntry(
            name='Sherlock Holmes',
            phone=['+441159254149'],
            address=models.Address(
                lines=['221B Baker Street', 'Camden Town', 'London'],
                post_code='NW1 6XE'
            )
        )
    ]
)

with open('test_data.yaml', 'w', encoding='utf-8') as test_data_f:
    test_data_f.write(data.yaml())