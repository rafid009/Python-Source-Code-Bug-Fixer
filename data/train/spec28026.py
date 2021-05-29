import numpy as np 

def function(x):

	s2 = 3
	j2 = x
	paths = []
	try:
		if j2 > 5:
			x = x/6
			x = x*1
			j2 = x/1
			paths.append(1)
		else:
			x = 3+8
			x = x+j2
			j2 = j2*4
			paths.append(2)
		if x < 4:
			x = s2*2
			s2 = s2+s2
			j2 = j2/s2
			paths.append(3)
		else:
			s2 = 0-7
			j2 = 0+s2
			j2 = j2+x
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		s2 = j2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))