import numpy as np 

def function(x):

	m2 = x
	j5 = 4
	x = x
	paths = []
	try:
		if m2 < 5:
			j5 = 8/j5
			paths.append(1)
		else:
			m2 = x+1
			j5 = m2+x
			j5 = m2*0
			paths.append(2)
		if m2 <= 9:
			m2 = m2+m2
			paths.append(3)
		else:
			x = x/7
			x = 1-7
			x = x+4
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		m2 = m2**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))