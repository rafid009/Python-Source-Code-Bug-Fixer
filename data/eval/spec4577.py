import numpy as np 

def function(x):

	n1 = x
	f3 = x
	paths = []
	try:
		if x <= 4:
			n1 = 0/n1
			paths.append(1)
		else:
			f3 = 0+f3
			n1 = n1*f3
			paths.append(2)
		if f3 < 8:
			n1 = n1*n1
			paths.append(3)
		else:
			n1 = 6*6
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