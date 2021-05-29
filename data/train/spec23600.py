import numpy as np 

def function(x):

	w5 = 0
	f8 = 1
	paths = []
	try:
		if w5 >= 2:
			f8 = 4+f8
			f8 = f8+5
			f8 = 7+x
			paths.append(1)
		else:
			w5 = w5-2
			paths.append(2)
		if x <= 8:
			f8 = x/9
			f8 = 9*x
			w5 = x+x
			paths.append(3)
		else:
			x = 7*x
			w5 = 2*3
			x = x/6
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		f8 = f8**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))