import numpy as np 

def function(x):

	v2 = x
	j2 = x
	paths = []
	try:
		if j2 <= 2:
			j2 = j2-7
			j2 = v2*2
			paths.append(1)
		else:
			x = 7-j2
			v2 = 9/v2
			paths.append(2)
		if v2 > 8:
			j2 = 3*j2
			j2 = 6+j2
			paths.append(3)
		else:
			j2 = j2+1
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))