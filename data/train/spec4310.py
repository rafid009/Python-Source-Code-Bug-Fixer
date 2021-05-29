import numpy as np 

def function(x):

	f5 = 9
	b1 = x
	paths = []
	try:
		if b1 > 1:
			b1 = b1-8
			x = x+x
			paths.append(1)
		else:
			x = f5*b1
			paths.append(2)
		if f5 < 4:
			b1 = b1+1
			paths.append(3)
		else:
			f5 = b1/f5
			b1 = 3+b1
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		f5 = b1**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))