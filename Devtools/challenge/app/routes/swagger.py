doc_specs = {
  "swagger": "2.0",
  "info": {
    "description": "This is the Devtools Challenge backend developed on Flask.",
    "version": "1.0.0",
    "title": "Devtools Challenge - Backend API documentation",
    "termsOfService": "http://swagger.io/terms/",
    "contact": {
      "email": "reinaldo.ramos@mercadolivre.com"
    },
    "license": {
      "name": "Apache 2.0",
      "url": "http://soporte.adminml.com"
    }
  },
  "host": "localhost:8080",
  "basePath": "/",
  "tags": [
    {
      "name": "alert",
      "description": "Get info about the alerts"
    },
    {
      "name": "docs",
      "description": "Access this API documentation"
    },
    {
      "name": "server",
      "description": "Get info about the servers"
    }
  ],
  "schemes": [
    "http"
  ],
  "paths": {
    "/docs": {
      "get": {
        "tags": [
          "docs"
        ],
        "summary": "Access this API documentation",
        "description": "",
        "produces": [
          "text/html"
        ],
        "responses": {
          "200": {
            "description": "Swagger documentation frontend"
          },
          "404": {
            "description": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
          }
        }
      }
    },
    
    "/alert": {
      "get": {
        "tags": [
          "content"
        ],
        "summary": "Get parent pages and their children",
        "description": "Get parent pages and their children",
        "operationId": "addPet",
        "consumes": [
          "application/json",
          "application/xml"
        ],
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "lang",
            "description": "Space language",
            "required": True,
            "type": "string"
          },
          {
            "in": "query",
            "name": "user",
            "description": "User type",
            "required": True,
            "type": "integer"
          }          
        ],
        "responses": {
          "405": {
            "description": "Invalid input"
          }
        }
      }
    },

    "/alert/new": {
      "get": {
        "tags": [
          "content"
        ],
        "summary": "create new alert",
        "description": "",
        "produces": [
          "content/html"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "id_page",
            "description": "ID of Confluence page",
            "required": True,
            "type": "string"
          }
        ],
        "responses": {
          "400": {
            "description": "Invalid ID supplied"
          },
          "404": {
            "description": "Pet not found"
          },
          "405": {
            "description": "Validation exception"
          }
        }
      }
    },

    "/alert/edit/{alert}": {
      "get": {
        "tags": [
          "content"
        ],
        "summary": "Edit an existing alert",
        "description": "",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "in": "query",
            "name": "top",
            "description": "Limit 'top' amount results",
            "required": True,
            "type": "integer"
          },
          {
            "in": "query",
            "name": "lang",
            "description": "Space language",
            "required": True,
            "type": "string"
          },
          {
            "in": "query",
            "name": "user",
            "description": "User type",
            "required": True,
            "type": "integer"
          }           
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Pet"
              }
            }
          },
          "400": {
            "description": "Invalid status value"
          }
        },
        "security": [
          {
            "petstore_auth": [
              "write:pets",
              "read:pets"
            ]
          }
        ]
      }
    },
    "/alert/delete/{alert}": {
      "get": {
        "tags": [
          "search"
        ],
        "summary": "Returns pet inventories by status",
        "description": "Returns a map of status codes to quantities",
        "operationId": "getInventory",
        "produces": [
          "application/json"
        ],
        "parameters": [],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "object",
              "additionalProperties": {
                "type": "integer",
                "format": "int32"
              }
            }
          }
        },
        "security": [
          {
            "api_key": []
          }
        ]
      }
    },
    "/server": {
      "get": {
        "tags": [
          "search"
        ],
        "summary": "Get info about servers",
        "description": "",
        "operationId": "placeOrder",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "in": "body",
            "name": "body",
            "description": "order placed for purchasing the pet",
            "required": True,
            "schema": {
              "$ref": "#/definitions/Order"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/Order"
            }
          },
          "400": {
            "description": "Invalid Order"
          }
        }
      }
    },
    "/server/new": {
      "get": {
        "tags": [
          "search"
        ],
        "summary": "Create a new server",
        "description": "For valid response try integer IDs with value >= 1 and <= 10.         Other values will generated exceptions",
        "operationId": "getOrderById",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "orderId",
            "in": "path",
            "description": "ID of pet that needs to be fetched",
            "required": True,
            "type": "integer",
            "maximum": 10,
            "minimum": 1,
            "format": "int64"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/Order"
            }
          },
          "400": {
            "description": "Invalid ID supplied"
          },
          "404": {
            "description": "Order not found"
          }
        }
      }
    },
    "/server/edit/{id}": {
      "get": {
        "tags": [
          "search"
        ],
        "summary": "Update existing server",
        "description": "For valid response try integer IDs with value >= 1 and <= 10.         Other values will generated exceptions",
        "operationId": "getOrderById",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "orderId",
            "in": "path",
            "description": "ID of pet that needs to be fetched",
            "required": True,
            "type": "integer",
            "maximum": 10,
            "minimum": 1,
            "format": "int64"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/Order"
            }
          },
          "400": {
            "description": "Invalid ID supplied"
          },
          "404": {
            "description": "Order not found"
          }
        }
      }
    },
    "/server/delete/{id}": {
      "get": {
        "tags": [
          "search"
        ],
        "summary": "Delete existing server",
        "description": "For valid response try integer IDs with value >= 1 and <= 10.         Other values will generated exceptions",
        "operationId": "getOrderById",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "orderId",
            "in": "path",
            "description": "ID of pet that needs to be fetched",
            "required": True,
            "type": "integer",
            "maximum": 10,
            "minimum": 1,
            "format": "int64"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/Order"
            }
          },
          "400": {
            "description": "Invalid ID supplied"
          },
          "404": {
            "description": "Order not found"
          }
        }
      }
    },
    "/history/{username}": {
      "get": {
        "tags": [
          "history"
        ],
        "summary": "Get page historical",
        "description": "",
        "operationId": "getUserByName",
        "produces": [
          "application/xml",
          "application/json"
        ],
        "parameters": [
          {
            "name": "username",
            "in": "path",
            "description": "The name that needs to be fetched. Use user1 for testing. ",
            "required": True,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/User"
            }
          },
          "400": {
            "description": "Invalid username supplied"
          },
          "404": {
            "description": "User not found"
          }
        }
      }
    }
  },
  "securityDefinitions": {
    "petstore_auth": {
      "type": "oauth2",
      "authorizationUrl": "http://petstore.swagger.io/oauth/dialog",
      "flow": "implicit",
      "scopes": {
        "write:pets": "modify pets in your account",
        "read:pets": "read your pets"
      }
    },
    "api_key": {
      "type": "apiKey",
      "name": "api_key",
      "in": "header"
    }
  },
  "definitions": {
    "Order": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "petId": {
          "type": "integer",
          "format": "int64"
        },
        "quantity": {
          "type": "integer",
          "format": "int32"
        },
        "shipDate": {
          "type": "string",
          "format": "date-time"
        },
        "status": {
          "type": "string",
          "description": "Order Status",
          "enum": [
            "placed",
            "approved",
            "delivered"
          ]
        },
        "complete": {
          "type": "boolean",
          "default": False
        }
      },
      "xml": {
        "name": "Order"
      }
    },
    "Category": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "name": {
          "type": "string"
        }
      },
      "xml": {
        "name": "Category"
      }
    },
    "User": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "username": {
          "type": "string"
        },
        "firstName": {
          "type": "string"
        },
        "lastName": {
          "type": "string"
        },
        "email": {
          "type": "string"
        },
        "password": {
          "type": "string"
        },
        "phone": {
          "type": "string"
        },
        "userStatus": {
          "type": "integer",
          "format": "int32",
          "description": "User Status"
        }
      },
      "xml": {
        "name": "User"
      }
    },
    "Tag": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "name": {
          "type": "string"
        }
      },
      "xml": {
        "name": "Tag"
      }
    },
    "Pet": {
      "type": "object",
      "required": [
        "name",
        "photoUrls"
      ],
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "category": {
          "$ref": "#/definitions/Category"
        },
        "name": {
          "type": "string",
          "example": "doggie"
        },
        "photoUrls": {
          "type": "array",
          "xml": {
            "name": "photoUrl",
            "wrapped": True
          },
          "items": {
            "type": "string"
          }
        },
        "tags": {
          "type": "array",
          "xml": {
            "name": "tag",
            "wrapped": True
          },
          "items": {
            "$ref": "#/definitions/Tag"
          }
        },
        "status": {
          "type": "string",
          "description": "pet status in the store",
          "enum": [
            "available",
            "pending",
            "sold"
          ]
        }
      },
      "xml": {
        "name": "Pet"
      }
    },
    "ApiResponse": {
      "type": "object",
      "properties": {
        "code": {
          "type": "integer",
          "format": "int32"
        },
        "type": {
          "type": "string"
        },
        "message": {
          "type": "string"
        }
      }
    }
  },
  "externalDocs": {
    "description": "Find out more about Swagger",
    "url": "http://swagger.io"
  }
}