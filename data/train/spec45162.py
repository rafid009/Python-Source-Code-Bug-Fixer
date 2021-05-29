import numpy as np 

def function(x):

	m9 = 0
	j2 = x
	paths = []
	try:
		if x > 5:
			j2 = j2*2
			paths.append(1)
		else:
			x = j2-3
			x = j2*x
			x = x*3
			paths.append(2)
		if m9 >= 4:
			m9 = 1*m9
			paths.append(3)
		else:
			j2 = 5-x
			m9 = m9*1
			x = x+x
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