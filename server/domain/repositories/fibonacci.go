package repositories

import (
	"errors"
	"log"

	"github.com/sergiovenicio/grpc-server-example/domain/entities"
)

type FibonacciRepository struct {
	Calcs map[string]entities.CalcRequest
}

func (r *FibonacciRepository) Get(id string) (*entities.CalcRequest, error) {
	request, exists := r.Calcs[id]
	if !exists {
		return nil, errors.New("calc undefined")
	}

	return &request, nil
}

func (r *FibonacciRepository) Add(request *entities.CalcRequest) {
	log.Printf("[fibonacci_repository] Add (%v)", request)
	r.Calcs[request.Id] = *request
}

func NewFibonacciRepository() *FibonacciRepository {
	return &FibonacciRepository{
		Calcs: make(map[string]entities.CalcRequest),
	}
}
