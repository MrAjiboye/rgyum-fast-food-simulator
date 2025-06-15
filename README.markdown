# RGyUm Fast-Food Simulator

A Python-based command-line application simulating a fast-food restaurant's menu system. This project was developed as part of the CMM202 coursework to demonstrate skills in data manipulation with pandas and interactive program design.

## Features
- **Data Manipulation**: Loads and merges two CSV files (`menu.csv` and `foods.csv`) to create a unified menu with standardized food names.
- **Admin Mode**: Allows administrators to log in (username: `admin`, password: any number < 10) and add products to existing menu slots (max 8 per slot).
- **Customer Mode**: Enables users to purchase food items, process payments, and receive change, with inventory updates.
- **Error Handling**: Robust input validation to prevent crashes from invalid inputs.

## Prerequisites
- Python 3.6+
- pandas library (`pip install pandas`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rgyum-fast-food-simulator.git
   cd rgyum-fast-food-simulator
   ```
2. Install dependencies:
   ```bash
   pip install pandas
   ```

## Usage
Run the program using:
```bash
python fast_food_simulator.py
```

### Menu Options
1. **Log in (admin only)**: Enter `admin` as username and a number < 10 as password. Limited to 4 attempts.
2. **Add product (admin only)**: Add one product to a non-empty menu slot after logging in.
3. **Buy products**: Select a food item by menu number, pay the price, and receive change if applicable.
4. **Exit**: Terminate the program.

### Example
```
Welcome to the RGyUm Fast-Food Menu
1. Log in (admin only)
2. Add one more product (admin only)
3. Buy products
4. Exit
>> 3

Current menu:
menu_number        food  amount category  price
A1          Margherita     8.0    pizza   5.50
...
Enter menu number to buy product (e.g., B1): B1
The price of Big Mac is £4.25.
Enter payment amount: 5.00
Your change is £0.75.
There are now 5.0 Big Mac left.
```

## Project Structure
- `fast_food_simulator.py`: Main Python script containing the application logic.
- `requirements.txt`: Lists required Python libraries.
- `README.md`: Project documentation.
- `LICENSE`: MIT License for the project.

## Data Sources
- `menu.csv`: Contains menu numbers, food items, and quantities (hosted on Dropbox).
- `foods.csv`: Contains food names, categories, and prices (hosted on Dropbox).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Future Improvements
- Add a graphical user interface using Tkinter or PyQt.
- Support multiple items in a single purchase.
- Save inventory changes to a local CSV file.

## Acknowledgments
- Developed for CMM202 coursework.
- Thanks to the course instructors for providing the dataset and requirements.
