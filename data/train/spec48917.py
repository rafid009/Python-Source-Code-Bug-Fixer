import numpy as np 

def function(x):

	f4 = 2
	n7 = 5
	paths = []
	try:
		if f4 <= 6:
			x = x*x
			x = x*5
			n7 = n7/5
			paths.append(1)
		else:
			f4 = n7*2
			paths.append(2)
		if n7 > 9:
			n7 = 4/n7
			n7 = f4-4
			f4 = 2+f4
			paths.append(3)
		else:
			n7 = n7-x
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		f4 = n7**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))