from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            f'message from {message_name}',  # subject
            message,  # message
            message_email,  # from email
            ['dkosarevsky.mtt@gmail.com', ],  # to email
        )

        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def blog_details(request):
    return render(request, 'blog-details.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def service(request):
    return render(request, 'service.html', {})


def appointment(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']


        # send an email
        appointment = f'''
                        Name: {your_name},
                        Phone: {your_phone},
                        Address: {your_address},
                        Schedule: {your_schedule},
                        Date: {your_date},
                        Message: {your_message}
                    '''
        send_mail(
            f'Appointment Request from {your_name}',  # subject
            appointment,  # message
            your_email,  # from email
            ['dkosarevsky.mtt@gmail.com', ],  # to email
        )

        return render(request, 'appointment.html', {
            'your-name': your_name,
            'your-phone': your_phone,
            'your-email': your_email,
            'your-address': your_address,
            'your_schedule': your_schedule,
            'your_date': your_date,
            'your_message': your_message,
        })

    else:
        return render(request, 'home.html', {})
