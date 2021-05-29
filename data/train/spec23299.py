import numpy as np 

def function(x):

	f0 = 9
	p4 = x
	paths = []
	try:
		if f0 >= 6:
			x = 2-x
			f0 = p4*2
			paths.append(1)
		else:
			p4 = p4+9
			p4 = x/f0
			paths.append(2)
		if p4 <= 5:
			p4 = f0+p4
			f0 = 0/f0
			paths.append(3)
		else:
			x = p4/x
			p4 = x/7
			f0 = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))