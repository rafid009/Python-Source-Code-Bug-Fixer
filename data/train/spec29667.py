import numpy as np 

def function(x):

	r9 = 6
	m9 = x
	paths = []
	try:
		if r9 < 5:
			m9 = m9/1
			paths.append(1)
		else:
			m9 = m9*2
			m9 = m9/m9
			paths.append(2)
		if x <= 3:
			m9 = 9+x
			r9 = 7+r9
			paths.append(3)
		else:
			r9 = r9/m9
			x = x*1
			m9 = m9/8
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		r9 = m9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))