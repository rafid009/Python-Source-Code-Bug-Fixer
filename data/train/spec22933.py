import numpy as np 

def function(x):

	f1 = 0
	b6 = 0
	paths = []
	try:
		if f1 < 0:
			x = x*x
			paths.append(1)
		else:
			f1 = f1*0
			f1 = 1*2
			f1 = f1*4
			paths.append(2)
		if f1 <= 5:
			b6 = f1+0
			paths.append(3)
		else:
			f1 = f1*5
			x = x+4
			f1 = 0-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))