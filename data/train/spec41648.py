import numpy as np 

def function(x):

	f5 = 0
	u2 = x
	paths = []
	try:
		if f5 > 2:
			f5 = x*u2
			f5 = u2-7
			paths.append(1)
		else:
			u2 = u2-8
			u2 = u2/x
			f5 = f5*x
			paths.append(2)
		if x <= 4:
			u2 = 7/u2
			u2 = u2*0
			paths.append(3)
		else:
			u2 = u2+1
			x = u2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))