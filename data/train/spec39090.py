import numpy as np 

def function(x):

	p1 = 8
	u8 = 5
	paths = []
	try:
		if x > 8:
			p1 = 1-8
			paths.append(1)
		else:
			u8 = 3/p1
			x = x+1
			p1 = 9*0
			paths.append(2)
		if x >= 4:
			u8 = 6+p1
			x = x/4
			x = x*7
			paths.append(3)
		else:
			p1 = p1/1
			x = x*x
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		u8 = p1**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))