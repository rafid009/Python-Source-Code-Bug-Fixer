import numpy as np 

def function(x):

	f3 = x
	f7 = 7
	paths = []
	try:
		if f7 <= 3:
			f7 = 7*f7
			f3 = f7*9
			paths.append(1)
		else:
			f3 = 5/f3
			f3 = f3*2
			paths.append(2)
		if f7 >= 4:
			f3 = f3-4
			f3 = f3-0
			paths.append(3)
		else:
			f7 = f7*x
			x = 2/f7
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))