import datetime
import os

def generate_invoice(prices_data, order_quantity_per_item, output_directory):
    """
    Generates a sales ticket based on prices and order quantity.

    Args:
        prices_data (dict): A dictionary where keys are product names and values are prices per kg.
        order_quantity_per_item (float): The quantity in kg for each item in the order.
        output_directory (str): The directory where the ticket_caisse.txt file will be saved.
    """
    
    today = datetime.date.today().strftime("%d-%m-%Y")
    ticket_content = f"--- Ticket de Caisse ---\n"
    ticket_content += f"Date: {today}\n"
    ticket_content += "------------------------\n"
    ticket_content += f"{'Produit':<20} {'Qté (kg)':<10} {'Prix/kg':<10} {'Total':<10}\n"
    ticket_content += "--------------------------------------------------\n"

    grand_total = 0.0

    for product, price_per_kg in prices_data.items():
        item_total = price_per_kg * order_quantity_per_item
        grand_total += item_total
        ticket_content += f"{product:<20} {order_quantity_per_item:<10.2f} {price_per_kg:<10.2f} {item_total:<10.2f}\n"

    ticket_content += "--------------------------------------------------\n"
    ticket_content += f"{'TOTAL:':<42} {grand_total:<10.2f} €\n"
    ticket_content += "------------------------\n"

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)
    
    output_filename = os.path.join(output_directory, "ticket_caisse.txt")
    
    with open(output_filename, 'w') as f:
        f.write(ticket_content)
    
    print(f"Ticket generated successfully at: {output_filename}")


if __name__ == "__main__":
    prices = {
        "Saucisses": 12.0,  # €/kg
        "Côte de bœuf": 25.0, # €/kg
        "Jambon blanc": 15.0 # €/kg
    }
    
    order_quantity = 2.0 # kg for each item
    output_dir = "/mnt/mpathg/guittte/ia-software-studio/Boucherie" # Destination folder for ticket

    generate_invoice(prices, order_quantity, output_dir)
