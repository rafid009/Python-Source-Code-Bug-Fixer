import numpy as np 

def function(x):

	f0 = x
	d4 = 1
	paths = []
	try:
		if d4 <= 8:
			d4 = 9*0
			paths.append(1)
		else:
			d4 = d4/1
			paths.append(2)
		if d4 >= 7:
			d4 = 1+d4
			x = x+f0
			paths.append(3)
		else:
			x = 7-x
			x = 4/8
			f0 = x*f0
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))