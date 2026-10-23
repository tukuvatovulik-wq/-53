from django.db import migrations, models

def fill_existing_details(apps, schema_editor):
    Task = apps.get_model("tasks", "Task")
    for task in Task.objects.filter(details=""):
        task.details = f"Подробности задачи: {task.description}"
        task.save(update_fields=["details"])

class Migration(migrations.Migration):
    dependencies = [("tasks", "0001_initial")]
    operations = [
        migrations.AddField(model_name="task", name="details", field=models.TextField(blank=True, default="", verbose_name="Подробное описание"), preserve_default=False),
        migrations.RunPython(fill_existing_details, migrations.RunPython.noop),
    ]
