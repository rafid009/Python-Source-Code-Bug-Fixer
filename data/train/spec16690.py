import numpy as np 

def function(x):

	b3 = x
	j2 = x
	paths = []
	try:
		if x < 9:
			j2 = j2/8
			x = 2*6
			j2 = j2+j2
			paths.append(1)
		else:
			b3 = 4/j2
			j2 = x/8
			paths.append(2)
		if b3 < 9:
			b3 = 0/x
			j2 = j2*x
			x = j2+9
			paths.append(3)
		else:
			b3 = b3*1
			x = x*b3
			j2 = 2*0
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		j2 = j2**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))