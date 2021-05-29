import numpy as np 

def function(x):

	f2 = x
	p4 = x
	paths = []
	try:
		if x < 5:
			p4 = 2/p4
			p4 = p4/5
			p4 = p4*4
			paths.append(1)
		else:
			p4 = 9/p4
			paths.append(2)
		if f2 > 4:
			x = f2/3
			x = 8*x
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		f2 = f2**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))