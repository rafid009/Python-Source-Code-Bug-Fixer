import numpy as np 

def function(x):

	f1 = x
	p1 = 4
	paths = []
	try:
		if f1 >= 4:
			p1 = 6*2
			f1 = f1/2
			paths.append(1)
		else:
			f1 = p1*f1
			f1 = 0*f1
			f1 = 7+f1
			paths.append(2)
		if x <= 2:
			f1 = f1*f1
			f1 = f1+0
			paths.append(3)
		else:
			p1 = 5-8
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		p1 = p1**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))