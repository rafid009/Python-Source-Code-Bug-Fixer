import numpy as np 

def function(x):

	w1 = 6
	f0 = x
	x = x
	paths = []
	try:
		if x >= 4:
			f0 = x/w1
			w1 = 5-w1
			x = 5/w1
			paths.append(1)
		else:
			x = 5+f0
			f0 = f0+x
			paths.append(2)
		if f0 > 2:
			f0 = f0/f0
			f0 = 1+f0
			paths.append(3)
		else:
			x = 4/9
			w1 = 6+f0
			f0 = f0-7
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