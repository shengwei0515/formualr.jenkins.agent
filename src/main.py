import click
import config

@click.command()
@click.option('-t',
              '--type',
              'type',
              help='Which type server you want to run, value can be "receiver" or sender',
              required=True)
def main(type):
    if type.lower() == 'receiver':
        import api_receiver.api_receiver as api_receiver
        api_receiver.app.run(host=config.API_HOST,port=config.API_PORT, debug=True)
    elif type.lower() == 'sender':
        import api_sender.formular_api_sender as api_sender
        print("start listening mq...")
        api_sender.mqclient.channel.start_consuming()
    else:
        raise 




if __name__ == '__main__':
    main()