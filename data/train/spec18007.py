import numpy as np 

def function(x):

	f7 = x
	w5 = x
	paths = []
	try:
		if f7 <= 2:
			w5 = w5*8
			f7 = f7-2
			paths.append(1)
		else:
			w5 = w5/w5
			x = f7/5
			paths.append(2)
		if f7 > 7:
			w5 = w5+4
			paths.append(3)
		else:
			f7 = x+w5
			x = 8/w5
			w5 = w5-8
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))