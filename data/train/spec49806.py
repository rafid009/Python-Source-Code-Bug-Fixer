import numpy as np 

def function(x):

	g5 = x
	f1 = x
	paths = []
	try:
		if x > 8:
			x = 0/2
			g5 = g5-8
			paths.append(1)
		else:
			x = 2/f1
			f1 = f1/3
			paths.append(2)
		if f1 <= 3:
			g5 = x*0
			paths.append(3)
		else:
			x = x*x
			g5 = 8/f1
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))