import numpy as np 

def function(x):

	j2 = 6
	r3 = x
	paths = []
	try:
		if x <= 3:
			r3 = 4*8
			x = r3*0
			paths.append(1)
		else:
			j2 = 4*x
			paths.append(2)
		if x >= 9:
			r3 = r3*r3
			x = x+9
			paths.append(3)
		else:
			j2 = j2*8
			r3 = 5*r3
			r3 = 7-j2
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))