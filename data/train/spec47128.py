import numpy as np 

def function(x):

	b1 = 4
	h7 = x
	paths = []
	try:
		if x <= 0:
			h7 = b1+6
			b1 = b1-3
			h7 = h7*0
			paths.append(1)
		else:
			h7 = h7+1
			b1 = 8/2
			paths.append(2)
		if b1 > 1:
			b1 = b1-8
			h7 = h7*2
			b1 = b1/6
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		x = b1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))