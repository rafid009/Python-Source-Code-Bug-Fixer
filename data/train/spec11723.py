import numpy as np 

def function(x):

	b1 = x
	r7 = 0
	paths = []
	try:
		if x < 5:
			b1 = b1+9
			paths.append(1)
		else:
			b1 = r7*0
			b1 = b1*r7
			b1 = x-b1
			paths.append(2)
		if b1 >= 8:
			x = x-x
			x = 5+x
			paths.append(3)
		else:
			b1 = x+b1
			r7 = x*r7
			r7 = b1+r7
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		r7 = b1**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))